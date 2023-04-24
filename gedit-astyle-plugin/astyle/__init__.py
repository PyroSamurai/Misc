# Gedit AStyle Plugin
# Copyright (c) 2017-2019 - The GNOME Project
#
# This program is libre software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("PeasGtk", "1.0")
from gi.repository import Gtk,GObject,Gio,PeasGtk,Gedit
import subprocess, os
from subprocess import Popen, PIPE

HOME = os.path.expanduser("~")
FILENAME = HOME+"/.config/gedit/astyle"
ACCELERATOR = ["<Shift>F8"]
STYLE = "allman"
STYLES = ["1tbs", "banner", "allman", "gnu", "google", "horstmann", "java",
          "kr", "linux", "lisp", "pico", "stroustrup", "whitesmith"]

# ################# FUNCTIONS ##################
def save_setting(TALK):
    global STYLE
    global FILENAME
    w_file = open(FILENAME, "w")
    w_file.write(TALK)
    w_file.close()

def load_setting():
    global FILENAME
    if os.path.isfile(FILENAME):
        r_file = open(FILENAME, "r")
        LSTYLE = r_file.read()
        r_file.close()
    else:
        LSTYLE = "allman"
        save_setting(LSTYLE)
    return LSTYLE


# ################# MENU ##################
class App(GObject.Object, Gedit.AppActivatable, PeasGtk.Configurable):
    __gtype_name__ = "AStyle"
    app = GObject.property(type=Gedit.App)

    def __init__(self):
        global STYLE
        GObject.Object.__init__(self)
        STYLE = load_setting()

    def do_activate(self):
        self.app.set_accels_for_action("win.astyle", ACCELERATOR)
        self.menu_ext = self.extend_menu("tools-section")
        item = Gio.MenuItem.new(_("AStyle"), "win.astyle")
        self.menu_ext.prepend_menu_item(item)

    def do_deactivate(self):
        self.app.set_accels_for_action("win.astyle", [])
        self.menu_ext = None

    def do_update_state(self):
        pass


# ################# ACTION ##################
class AppWindow(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        global STYLE
        GObject.Object.__init__(self)
        self.settings = Gio.Settings.new("org.gnome.gedit.preferences.editor")
        STYLE = load_setting()

    def do_activate(self):
        action = Gio.SimpleAction(name="astyle")
        action.connect("activate", self.format_code)
        self.window.add_action(action)

    def formatter(self, code):
        global STYLE
        view = self.window.get_active_view()
        tabLen = str(view.get_tab_width())
        maxLen = str(view.get_right_margin_position())
        options = "-xC"+maxLen+" -U -c -s"+tabLen
        cmd = ["astyle --style="+STYLE+" "+options]
        proc = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
        proc.stdin.write(bytes(code, "utf-8"))
        proc.stdin.close()
        return proc.stdout.read()

    def format_code(self, action, parameter, user_data=None):
        global STYLE
        doc = self.window.get_active_document()
        start, end = doc.get_bounds()
        code = doc.get_text(start, end, True)
        result = self.formatter(code)
        doc.set_text(str(result, "utf-8"))

