import ctypes
import sys

_AVAILABLE = False
_PRELOADED_SELECTORS = {}
_OBJC = None


def _init_objc():
    global _AVAILABLE, _OBJC
    if _AVAILABLE or _OBJC is not None:
        return _AVAILABLE
    if sys.platform != "darwin":
        return False
    try:
        lib = ctypes.cdll.LoadLibrary("/usr/lib/libobjc.dylib")
        lib.objc_getClass.restype = ctypes.c_void_p
        lib.objc_getClass.argtypes = [ctypes.c_char_p]
        lib.sel_registerName.restype = ctypes.c_void_p
        lib.sel_registerName.argtypes = [ctypes.c_char_p]
        _OBJC = lib
        _AVAILABLE = True
    except Exception:
        _AVAILABLE = False
    return _AVAILABLE


def _sel(name: str):
    if name in _PRELOADED_SELECTORS:
        return _PRELOADED_SELECTORS[name]
    sel = _OBJC.sel_registerName(name.encode("utf-8"))
    _PRELOADED_SELECTORS[name] = sel
    return sel


def _send_id(receiver: int, selector: str) -> int:
    f = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    return sender(receiver, _sel(selector))


def _get_ns_window(view_ptr: int) -> int:
    if not view_ptr:
        return 0
    return _send_id(view_ptr, "window")


def set_ignores_mouse_events(widget, enabled: bool):
    if not _init_objc() or widget is None:
        return
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return
    if not win_id:
        return
    window = _get_ns_window(win_id)
    if not window:
        return
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setIgnoresMouseEvents:"), ctypes.c_bool(enabled))


def set_window_level_floating(widget) -> bool:
    return _set_window_level(widget, 3)


def set_window_level_status_bar(widget) -> bool:
    # NSStatusWindowLevel — high enough that AppKit's constrainFrameRect:toScreen:
    # stops clamping the window to below the menu bar, so the user can drag the
    # pet anywhere on screen even when the visible character is offset inside
    # the window's transparent bounds.
    return _set_window_level(widget, 25)


def set_window_level_above_menu_bar(widget) -> bool:
    return _set_window_level(widget, 101)


def _set_window_level(widget, level: int) -> bool:
    if not _init_objc() or widget is None:
        return False
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return False
    if not win_id:
        return False
    window = _get_ns_window(win_id)
    if not window:
        return False
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setLevel:"), level)
    return True


def set_window_no_shadow(widget) -> bool:
    if not _init_objc() or widget is None:
        return False
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return False
    if not win_id:
        return False
    window = _get_ns_window(win_id)
    if not window:
        return False
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setHasShadow:"), ctypes.c_bool(False))
    return True


def set_hides_on_deactivate(widget, hides: bool) -> bool:
    # Qt.Tool maps to NSPanel on macOS, and NSPanel defaults to
    # hidesOnDeactivate:YES — so any time the user clicks another app the
    # window vanishes. Force it off so floating helpers stay visible.
    if not _init_objc() or widget is None:
        return False
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return False
    if not win_id:
        return False
    window = _get_ns_window(win_id)
    if not window:
        return False
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setHidesOnDeactivate:"), ctypes.c_bool(hides))
    return True


# NSWindowCollectionBehavior bits used by the pet window so it shows up across
# every Space and over fullscreen apps without joining the Cmd+~ cycle.
NS_COLLECTION_CAN_JOIN_ALL_SPACES = 1 << 0
NS_COLLECTION_STATIONARY = 1 << 4
NS_COLLECTION_IGNORES_CYCLE = 1 << 6
NS_COLLECTION_FULL_SCREEN_AUXILIARY = 1 << 8

PET_COLLECTION_BEHAVIOR = (
    NS_COLLECTION_CAN_JOIN_ALL_SPACES
    | NS_COLLECTION_STATIONARY
    | NS_COLLECTION_IGNORES_CYCLE
    | NS_COLLECTION_FULL_SCREEN_AUXILIARY
)


def set_collection_behavior(widget, mask: int) -> bool:
    if not _init_objc() or widget is None:
        return False
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return False
    if not win_id:
        return False
    window = _get_ns_window(win_id)
    if not window:
        return False
    # NSWindowCollectionBehavior is NSUInteger (unsigned long on 64-bit darwin).
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setCollectionBehavior:"), ctypes.c_ulong(int(mask)))
    return True


def hide_dock_icon():
    if sys.platform != "darwin":
        return
    try:
        from AppKit import NSApp, NSApplicationActivationPolicyAccessory
        NSApp.activateIgnoringOtherApps_(True)
        NSApp.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
        return
    except Exception:
        pass
    if not _init_objc():
        return
    try:
        app_class = _OBJC.objc_getClass(b"NSApplication")
        if not app_class:
            return
        app = _send_id(app_class, "sharedApplication")
        if not app:
            return
        f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long)
        sender = ctypes.cast(_OBJC.objc_msgSend, f)
        sender(app, _sel("setActivationPolicy:"), 1)
    except Exception:
        pass


def install_ns_status_item(icon_path: str, on_settings: callable, on_quit: callable) -> object:
    """Create a native NSStatusItem with a simple Settings / Quit menu.

    Returns the NSStatusItem (caller must keep a strong reference).
    """
    try:
        from AppKit import (
            NSApp,
            NSStatusBar,
            NSImage,
            NSMenu,
            NSMenuItem,
            NSVariableStatusItemLength,
        )
        import objc

        NSApp.activateIgnoringOtherApps_(True)

        class _MenuDelegate(objc.lookUpClass("NSObject")):
            @objc.python_method
            def setup(self, settings_cb, quit_cb):
                self._settings_cb = settings_cb
                self._quit_cb = quit_cb

            def openSettings_(self, sender):
                self._settings_cb()

            def quitApp_(self, sender):
                self._quit_cb()

        status_bar = NSStatusBar.systemStatusBar()
        item = status_bar.statusItemWithLength_(NSVariableStatusItemLength)
        button = item.button()

        if icon_path:
            img = NSImage.alloc().initWithContentsOfFile_(icon_path)
            if img is not None:
                img.setSize_((18, 18))
                button.setImage_(img)

        delegate = _MenuDelegate.alloc().init()
        delegate.setup(on_settings, on_quit)

        ns_menu = NSMenu.alloc().init()

        settings_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Settings", objc.selector(delegate.openSettings_, selector=b"openSettings:"), ""
        )
        settings_item.setTarget_(delegate)
        ns_menu.addItem_(settings_item)

        ns_menu.addItem_(NSMenuItem.separatorItem())

        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Quit", objc.selector(delegate.quitApp_, selector=b"quitApp:"), ""
        )
        quit_item.setTarget_(delegate)
        ns_menu.addItem_(quit_item)

        item.setMenu_(ns_menu)
        # Return a tuple so the caller holds strong refs to both objects.
        return (item, delegate)
    except Exception:
        return None


def set_becomes_key_only_if_needed(widget) -> bool:
    if not _init_objc() or widget is None:
        return False
    try:
        win_id = int(widget.winId())
    except (TypeError, ValueError):
        return False
    if not win_id:
        return False
    window = _get_ns_window(win_id)
    if not window:
        return False
    f = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)
    sender = ctypes.cast(_OBJC.objc_msgSend, f)
    sender(window, _sel("setBecomesKeyOnlyIfNeeded:"), ctypes.c_bool(True))
    return True


def is_available() -> bool:
    return _init_objc()
