"""
Primero comenzamos instalando los sigs. requisitos:

?$ apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev 
?$ libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev 
?$ libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev

Luego necesitamos instalar bspwm y sxhkd

?$ git clone https://github.com/baskerville/bspwm.git
?$ git clone https://github.com/baskerville/sxhkd.git

Dentro de cada uno 

?$ make 
?$ sudo make install

Luego descargamos bspwm

?$ sudo apt install bspwm

Como usuario no priv

?$ mkdir ~/.config/bspwm

?$ mkdir ~/.config/sxhkd

Dentro del repo bspwm

Copiar el archivo bspwmrc dentro de la carpeta creada en .config
y el sxhkd dentro de su respectiva carpeta creada 

?$ sudo apt install kitty
#!/.config/bspwm/bspwmrc

#! /bin/sh

pgrep -x sxhkd > /dev/null || sxhkd &

bspc monitor -d I II III IV V VI VII VIII IX X

bspc config border_width         2
bspc config window_gap          12

bspc config split_ratio          0.52
bspc config borderless_monocle   true
bspc config gapless_monocle      true

bspc rule -a Gimp desktop='^8' state=floating follow=on
bspc rule -a Chromium desktop='^2'
bspc rule -a mplayer2 state=floating
bspc rule -a Kupfer.py focus=on
bspc rule -a Screenkey manage=off

feh --bg-fill /home/dobliuw/Fondos/FondoDobliuw.png &
~/.config/polybar/./launch.sh
picom & 
xrandr --output HDMI-A-1 --mode 1920x1080 --rate 144.00
bspc config border_width 0

linea 55 fondo de pantalla --> sudo apt install feh
linea 58 ajuste monitor

#!/.config/sxhkd/sxhkdrc

  GNU nano 5.4                                                               /home/dobliuw/.config/sxhkd/sxhkdrc                                                                 I      
    bspc node -o 0.{1-9}

# cancel the preselection for the focused node
super + ctrl + alt + space
    bspc node -p cancel

# cancel the preselection for the focused desktop
super + ctrl + shift + space
    bspc query -N -d | xargs -I id -n 1 bspc node id -p cancel

#
# move/resize
#

# expand a window by moving one of its side outward
#super + alt + {h,j,k,l}
#   bspc node -z {left -20 0,bottom 0 20,top 0 -20,right 20 0}

# contract a window by moving one of its side inward
#super + alt + shift + {h,j,k,l}
#   bspc node -z {right -20 0,top 0 20,bottom 0 -20,left 20 0}

# move a floating window
super + ctrl + {Left,Down,Up,Right}
    bspc node -v {-20 0,0 20,0 -20,20 0}

# Custom resize
alt + super + {Left,Down,Up,Right}
    /home/dobliuw/.config/bspwm/scripts/bspwm_resize {west,south,north,east}

# Open firefox

super + shift + f
    /usr/bin/firefox

super + shift + x
  /usr/bin/i3lock-fancy

super + ctrl + c
  /usr/bin/flameshot gui


En la linea 65 indicamos un archivo el cual tenemos que crear

?$ touch /home/dobliuw/.config/bspwm/scripts/bspwm_resize

?$ nvim !$
------------
#!/usr/bin/env dash

if bspc query -N -n focused.floating > /dev/null; then
	step=20
else
	step=100
fi

case "$1" in
	west) dir=right; falldir=left; x="-$step"; y=0;;
	east) dir=right; falldir=left; x="$step"; y=0;;
	north) dir=top; falldir=bottom; x=0; y="-$step";;
	south) dir=top; falldir=bottom; x=0; y="$step";;
esac

bspc node -z "$dir" "$x" "$y" || bspc node -z "$falldir" "$x" "$y"
------------

Instalamos la polybar

?$ apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev 
?$ libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto 
?$ libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev
?$ libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev 
?$ libuv1-dev libnl-genl-3-dev

?$ git clone -–recursive https://github.com/polybar/polybar

Dentro del repo  bajado 

?$ mkdir  build

?$ cd !$

?$ cmake ..

?$ make -j$(nproc)

?$ sudo make install 

Toca instalar picom 

?$ apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev 
?$ libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-composite0-dev 
?$ libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev 
?$ libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev 
?$ libev-dev libx11-xcb-dev libxcb-glx0-dev

?$ git clone https://github.com/ibhagwan/picom.git

Dentro:

?$ git submodule update --init --recursive

?$ meson --buildtype=release

?$ ninja -C build 

?$ sudo ninja -C build installa

Rofi:

?$ apt install rofi

Font hack nerd font:

?$ cd /usr/local/share/fonts

?$ unzip Hack.zip

Kitty:

/.config/kitty/color.ini

--------
cursor_shape          Underline
cursor_underline_thickness 1
window_padding_width  20

# Special
foreground #a9b1d6
background #1a1b26

# Black
color0 #414868
color8 #414868

# Red
color1 #f7768e
color9 #f7768e

# Green
color2  #73daca
color10 #73daca

# Yellow
color3  #e0af68
color11 #e0af68

# Blue
color4  #7aa2f7
color12 #7aa2f7

# Magenta
color5  #bb9af7
color13 #bb9af7

# Cyan
color6  #7dcfff
color14 #7dcfff

# White
color7  #c0caf5
color15 #c0caf5

# Cursor
cursor #c0caf5
cursor_text_color #1a1b26

# Selection highlight
selection_foreground #7aa2f7
selection_background #28344a

/.config/kitty/kitty.conf

  GNU nano 5.4               /home/dobliuw/.config/kitty/kitty.conf                  I      

url_color #61afef

url_style curly

map ctrl+left neighboring_window left
map ctrl+right neighboring_window right
map ctrl+up neighboring_window up
map ctrl+down neighboring_window down

map f1 copy_to_buffer a
map f2 paste_from_buffer a
map f3 copy_to_buffer b
map f4 paste_from_buffer b

cursor_shape beam
cursor_beam_thickness 1.8

mouse_hide_wait 3.0
detect_urls yes

repaint_delay 10
input_delay 3
sync_to_monitor yes

map ctrl+shift+z toggle_layout stack
tab_bar_style powerline

inactive_tab_background #e06c75
active_tab_background #98c379
inactive_tab_foreground #000000
tab_bar_margin_color black

map ctrl+shift+enter new_window_with_cwd
map ctrl+shift+t new_tab_with_cwd

background_opacity 0.95

shell zsh
------

?$ sudo apt install zsh

?$ sudo apt install zsh-autcomplete
?$ sudo apt install zsh-autosuggestions
?$ sudo apt install zsh-syntax-highlighting

hacer backup de la conf de kitty, ir a github 

"https://kovidgoyala/kitty/releases" ---> Linux amd64 binary bundle

en /opt

mkdir kitty  ---> chown user:user kitty/

mv --> Linux amd64 binary bundle ---> opt/kitty

?$ tar -xf Linux amd64 binary bundle

?$ nano ~/.config/sxhkd/sxhkdrx 

ruta absoluta del binario instalado 

Recordar que root tiene otra consola, otra zshrc, etc

?$ sudo apt install imagemagick

?$ git clone https:&//github.com/VaughValle/blue-sky.git

cd en lo descargado 

?$ cp * -r ~/.config/polybar

?$ cd !$

?$ echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc

Copiar todas las fuented de /blue-sky/polybar/fonts

?$ sudo cp * /usr/share/fonts/truetype

fc-cache -v ---> "succeeded"

Configurando picom 

mkdir --> /.config  --> picom 

##############################################################################
#                                  CORNERS                                   #
##############################################################################
# requires: https://github.com/sdhand/compton
corner-radius = 20;
rounded-corners-exclude = [
  #"window_type = 'normal'",
  #"class_g = 'firefox'",
];

round-borders = 20;
round-borders-exclude = [
  #"class_g = 'TelegramDesktop'",
];

# Specify a list of border width rules, in the format `PIXELS:PATTERN`, 
# Note we don't make any guarantee about possible conflicts with the
# border_width set by the window manager.
#
# example:
#    round-borders-rule = [ "2:class_g = 'URxvt'" ];
#
round-borders-rule = [];

##############################################################################
#                                  SHADOWS                                   #
##############################################################################

# Enabled client-side shadows on windows. Note desktop windows 
# (windows with '_NET_WM_WINDOW_TYPE_DESKTOP') never get shadow, 
# unless explicitly requested using the wintypes option.
#
shadow = true

# The blur radius for shadows, in pixels. (defaults to 12)
shadow-radius = 15

# The opacity of shadows. (0.0 - 1.0, defaults to 0.75)
shadow-opacity = .5

# The left offset for shadows, in pixels. (defaults to -15)
shadow-offset-x = -15

# The top offset for shadows, in pixels. (defaults to -15)
shadow-offset-y = -15

# Avoid drawing shadows on dock/panel windows. This option is deprecated,
# you should use the *wintypes* option in your config file instead.
#
# no-dock-shadow = false

# Don't draw shadows on drag-and-drop windows. This option is deprecated, 
# you should use the *wintypes* option in your config file instead.
#
# no-dnd-shadow = false

# Red color value of shadow (0.0 - 1.0, defaults to 0).
# shadow-red = .18

# Green color value of shadow (0.0 - 1.0, defaults to 0).
# shadow-green = .19

# Blue color value of shadow (0.0 - 1.0, defaults to 0).
# shadow-blue = .20

# Do not paint shadows on shaped windows. Note shaped windows 
# here means windows setting its shape through X Shape extension. 
# Those using ARGB background is beyond our control. 
# Deprecated, use 
#   shadow-exclude = 'bounding_shaped'
# or 
#   shadow-exclude = 'bounding_shaped && !rounded_corners'
# instead.
#
# shadow-ignore-shaped = ''

# Specify a list of conditions of windows that should have no shadow.
#
# examples:
#   shadow-exclude = "n:e:Notification";
#
# shadow-exclude = []
shadow-exclude = [
    "class_g = 'firefox' && argb"
];

# Specify a X geometry that describes the region in which shadow should not
# be painted in, such as a dock window region. Use 
#    shadow-exclude-reg = "x10+0+0"
# for example, if the 10 pixels on the bottom of the screen should not have shadows painted on.
#
# shadow-exclude-reg = "" 

# Crop shadow of a window fully on a particular Xinerama screen to the screen.
# xinerama-shadow-crop = false

##############################################################################
#                                  FADING                                    #
##############################################################################

# Fade windows in/out when opening/closing and when opacity changes,
#  unless no-fading-openclose is used.
#fading = true

# Opacity change between steps while fading in. (0.01 - 1.0, defaults to 0.028)
# fade-in-step = 0.028
fade-in-step = 0.01;

# Opacity change between steps while fading out. (0.01 - 1.0, defaults to 0.03)
# fade-out-step = 0.03
fade-out-step = 0.01;

# The time between steps in fade step, in milliseconds. (> 0, defaults to 10)
# fade-delta = 10

# Specify a list of conditions of windows that should not be faded.
# fade-exclude = []

# Do not fade on window open/close.
# no-fading-openclose = false

# Do not fade destroyed ARGB windows with WM frame. Workaround of bugs in Openbox, Fluxbox, etc.
# no-fading-destroyed-argb = false

##############################################################################
#                                   OPACITY                                  #
##############################################################################

# Opacity of inactive windows. (0.1 - 1.0, defaults to 1.0)
inactive-opacity = 1.0

# Opacity of window titlebars and borders. (0.1 - 1.0, disabled by default)
frame-opacity = 1.0

# Default opacity for dropdown menus and popup menus. (0.0 - 1.0, defaults to 1.0)
opacity = 1.0

# Let inactive opacity set by -i override the '_NET_WM_OPACITY' values of windows.
# inactive-opacity-override = true
inactive-opacity-override = false;

# Default opacity for active windows. (0.0 - 1.0, defaults to 1.0)
active-opacity = 1.0

# Dim inactive windows. (0.0 - 1.0, defaults to 0.0)
# inactive-dim = 0.0

# Specify a list of conditions of windows that should always be considered focused.
# focus-exclude = []
focus-exclude = [ "class_g = 'Cairo-clock'" ];

# Use fixed inactive dim value, instead of adjusting according to window opacity.
# inactive-dim-fixed = 1.0

# Specify a list of opacity rules, in the format `PERCENT:PATTERN`, 
# like `50:name *= "Firefox"`. picom-trans is recommended over this. 
# Note we don't make any guarantee about possible conflicts with other 
# programs that set '_NET_WM_WINDOW_OPACITY' on frame or client windows.
# example:
#    opacity-rule = [ "80:class_g = 'URxvt'" ];
#
# opacity-rule = []

# opacity-rule = [ "98:class_g = 'Polybar'" ]

##############################################################################
#                                    BLUR                                    #
##############################################################################

# Parameters for background blurring, see the *BLUR* section for more information.
blur-method = "dual_kawase"
blur-size = 2
blur-strength = 3

# Blur background of semi-transparent / ARGB windows. 
# Bad in performance, with driver-dependent behavior. 
# The name of the switch may change without prior notifications.
#
blur-background = true

# Blur background of windows when the window frame is not opaque. 
# Implies:
#    blur-background 
# Bad in performance, with driver-dependent behavior. The name may change.
#
#blur-background-frame = false


# Use fixed blur strength rather than adjusting according to window opacity.
#blur-background-fixed = false


# Specify the blur convolution kernel, with the following format:
# example:
#   blur-kern = "5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1";
#
# blur-kern = ''
# blur-kern = "3x3box";

# Exclude conditions for background blur.
# blur-background-exclude = []
#blur-background-exclude = [
#    "! name~=''",
#    "name *= 'slop'",
#    "window_type = 'dock'",
#    "window_type = 'desktop'",
#    "_GTK_FRAME_EXTENTS@:c"
#];

##############################################################################
#                                    GENERAL                                 #
##############################################################################

# Daemonize process. Fork to background after initialization. Causes issues with certain (badly-written) drivers.
# daemon = false

# Specify the backend to use: `xrender`, `glx`, or `xr_glx_hybrid`.
# `xrender` is the default one.
#
# backend = 'glx'
backend = "glx";

# Enable/disable VSync.
# vsync = false
vsync = false

# Enable remote control via D-Bus. See the *D-BUS API* section below for more details.
# dbus = false

# Try to detect WM windows (a non-override-redirect window with no 
# child that has 'WM_STATE') and mark them as active.
#
# mark-wmwin-focused = false
mark-wmwin-focused = true;

# Mark override-redirect windows that doesn't have a child window with 'WM_STATE' focused.
# mark-ovredir-focused = false
mark-ovredir-focused = true;

# Try to detect windows with rounded corners and don't consider them 
# shaped windows. The accuracy is not very high, unfortunately.
#
# detect-rounded-corners = false
detect-rounded-corners = true;

# Detect '_NET_WM_OPACITY' on client windows, useful for window managers
# not passing '_NET_WM_OPACITY' of client windows to frame windows.
#
# detect-client-opacity = false
detect-client-opacity = true;

# Specify refresh rate of the screen. If not specified or 0, picom will 
# try detecting this with X RandR extension.
#
# refresh-rate = 60
refresh-rate = 0

# Limit picom to repaint at most once every 1 / 'refresh_rate' second to 
# boost performance. This should not be used with 
#   vsync drm/opengl/opengl-oml
# as they essentially does sw-opti's job already, 
# unless you wish to specify a lower refresh rate than the actual value.
#
# sw-opti = 

# Use EWMH '_NET_ACTIVE_WINDOW' to determine currently focused window, 
# rather than listening to 'FocusIn'/'FocusOut' event. Might have more accuracy, 
# provided that the WM supports it.
#
# use-ewmh-active-win = false

# Unredirect all windows if a full-screen opaque window is detected, 
# to maximize performance for full-screen windows. Known to cause flickering 
# when redirecting/unredirecting windows.
#
# unredir-if-possible = false

# Delay before unredirecting the window, in milliseconds. Defaults to 0.
# unredir-if-possible-delay = 0

# Conditions of windows that shouldn't be considered full-screen for unredirecting screen.
# unredir-if-possible-exclude = []

# Use 'WM_TRANSIENT_FOR' to group windows, and consider windows 
# in the same group focused at the same time.
#
# detect-transient = false
detect-transient = true

# Use 'WM_CLIENT_LEADER' to group windows, and consider windows in the same 
# group focused at the same time. 'WM_TRANSIENT_FOR' has higher priority if 
# detect-transient is enabled, too.
#
# detect-client-leader = false
detect-client-leader = true

# Resize damaged region by a specific number of pixels. 
# A positive value enlarges it while a negative one shrinks it. 
# If the value is positive, those additional pixels will not be actually painted 
# to screen, only used in blur calculation, and such. (Due to technical limitations, 
# with use-damage, those pixels will still be incorrectly painted to screen.) 
# Primarily used to fix the line corruption issues of blur, 
# in which case you should use the blur radius value here 
# (e.g. with a 3x3 kernel, you should use `--resize-damage 1`, 
# with a 5x5 one you use `--resize-damage 2`, and so on). 
# May or may not work with *--glx-no-stencil*. Shrinking doesn't function correctly.
#
# resize-damage = 1

# Specify a list of conditions of windows that should be painted with inverted color. 
# Resource-hogging, and is not well tested.
#
# invert-color-include = []

# GLX backend: Avoid using stencil buffer, useful if you don't have a stencil buffer. 
# Might cause incorrect opacity when rendering transparent content (but never 
# practically happened) and may not work with blur-background. 
# My tests show a 15% performance boost. Recommended.
#
# glx-no-stencil = false

# GLX backend: Avoid rebinding pixmap on window damage. 
# Probably could improve performance on rapid window content changes, 
# but is known to break things on some drivers (LLVMpipe, xf86-video-intel, etc.).
# Recommended if it works.
#
# glx-no-rebind-pixmap = false

# Disable the use of damage information. 
# This cause the whole screen to be redrawn everytime, instead of the part of the screen
# has actually changed. Potentially degrades the performance, but might fix some artifacts.
# The opposing option is use-damage
#
# no-use-damage = false
use-damage = false

# Use X Sync fence to sync clients' draw calls, to make sure all draw 
# calls are finished before picom starts drawing. Needed on nvidia-drivers 
# with GLX backend for some users.
#
# xrender-sync-fence = false

# GLX backend: Use specified GLSL fragment shader for rendering window contents. 
# See `compton-default-fshader-win.glsl` and `compton-fake-transparency-fshader-win.glsl` 
# in the source tree for examples.
#
# glx-fshader-win = ''

# Force all windows to be painted with blending. Useful if you 
# have a glx-fshader-win that could turn opaque pixels transparent.
#
# force-win-blend = false

# Do not use EWMH to detect fullscreen windows. 
# Reverts to checking if a window is fullscreen based only on its size and coordinates.
#
# no-ewmh-fullscreen = false

# Dimming bright windows so their brightness doesn't exceed this set value. 
# Brightness of a window is estimated by averaging all pixels in the window, 
# so this could comes with a performance hit. 
# Setting this to 1.0 disables this behaviour. Requires --use-damage to be disabled. (default: 1.0)
#
# max-brightness = 1.0

# Make transparent windows clip other windows like non-transparent windows do,
# instead of blending on top of them.
#
# transparent-clipping = false

# Set the log level. Possible values are:
#  "trace", "debug", "info", "warn", "error"
# in increasing level of importance. Case doesn't matter. 
# If using the "TRACE" log level, it's better to log into a file 
# using *--log-file*, since it can generate a huge stream of logs.
#
# log-level = "debug"
log-level = "warn";

# Set the log file.
# If *--log-file* is never specified, logs will be written to stderr. 
# Otherwise, logs will to written to the given file, though some of the early 
# logs might still be written to the stderr. 
# When setting this option from the config file, it is recommended to use an absolute path.
#
# log-file = '/path/to/your/log/file'

# Show all X errors (for debugging)
# show-all-xerrors = false

# Write process ID to a file.
# write-pid-path = '/path/to/your/log/file'

# Window type settings
# 
# 'WINDOW_TYPE' is one of the 15 window types defined in EWMH standard: 
#     "unknown", "desktop", "dock", "toolbar", "menu", "utility", 
#     "splash", "dialog", "normal", "dropdown_menu", "popup_menu", 
#     "tooltip", "notification", "combo", and "dnd".
# 
# Following per window-type options are available: ::
# 
#   fade, shadow:::
#     Controls window-type-specific shadow and fade settings.
# 
#   opacity:::
#     Controls default opacity of the window type.
# 
#   focus:::
#     Controls whether the window of this type is to be always considered focused. 
#     (By default, all window types except "normal" and "dialog" has this on.)
# 
#   full-shadow:::
#     Controls whether shadow is drawn under the parts of the window that you 
#     normally won't be able to see. Useful when the window has parts of it 
#     transparent, and you want shadows in those areas.
# 
#   redir-ignore:::
#     Controls whether this type of windows should cause screen to become 
#     redirected again after been unredirected. If you have unredir-if-possible
#     set, and doesn't want certain window to cause unnecessary screen redirection, 
#     you can set this to `true`.
#
wintypes:
{
  tooltip = { fade = true; shadow = true; shadow-radius = 0; shadow-opacity = 1.0; shadow-offset-x = -20; shadow-offset-y = -20; opacity = 0.8; full-shadow = true; }; 
  dnd = { shadow = false; }
  dropdown_menu = { shadow = false; };
  popup_menu    = { shadow = false; };
  utility       = { shadow = false; };
}
------

Powerlevel10k ---> p10k configure

?$  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
?$  echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc

nano ~/.p10k.zsh

Comentar todo lo de la derecha, agregar
command_execution_time, status, context

Shell para el root

?$ usermod --shell /usr/bin/zsh root

?$ chown root:root /usr/local/share/zsh/site-functions/_bspc

Enlace simbolico 

?$ kn -s -f apuntado apunta

bat --no-paging

Rofi:

?$ git clone https:&//github.com/VaughValle/blue-sky.git

?$ cd nlu-sky

mkdir -p ~/.config/rofi/themes
cp nord.rasi ~/.config/rofi/themes
rofi-themes-selector 
alt + a 



"""

