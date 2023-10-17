"""

Time timestamps date and chronological reality

"""


import os as                        os
import sys as                       sys
import tkinter as                   tk
from   tkinter import               ttk
from   tkinter import               font
from   PIL import Image     as      pl
from   PIL import ImageTk   as      ii
from   tkinter import filedialog as fd
from   tkinter.messagebox import    showinfo
from   tokenize import              maybe
from   datetime import              datetime


# Imports part of this program 
import aboutTime as         tt      # Time dates timestamps and the like
import avMedia as           av      # Audio and maybe video 'someday' well definitely lots of TTS text to speech
import basicSwitchboard as  sc      # First switchboard always lurking. Kickoff to sequence viewers
import bestNotifications as bn      # Alerts, modals and notifications of many kinds including TK windows
import bitBlitting as       bb      # Help - # A setup window with basic facts written into files and the workspace
import configSetting as     cs      # A setup window with basic facts written into files and the workspace
import devPeeks as          dp      # Developments peek assets code for adding features and debugging
import fileIo as            io      # File reads, writes even some of the the pickle and unpickling
import forFun as            ff      # Staging area for uncertian features, also some dynamic code inclusion
import fractionScreens as   fs      # Common window pieces for TK windows in sequence viewers
import genomeDb as          gd      # IO to from databases external files gbk and others sure
import globalIdeas as       gi      # Common code for stuff used everywhere and definition of share DOT OBJECTS
import insertableEditors as ie      # Text editor(s) and support for that, some language issues managed too
import modalSimple as       mo      # Modal windows icp seq ssues, not used much currently
import osDependant as       od      # Operating system dependant calls and adaptions
import pickle as            pk      # Packaging to and from file system for objects especially DOT OBJECTS
import screenBuilder1 as    sb      # Screen maker for TKinter and TKinter ++ windows
import selectViewer as      sv      # Window for picking which sequence viewers are enabled
import sequencesMaintain as sm      # Touching up temporal version issues of DOT OBJECTS
import sequencesOverview as so      # Working with sequences as macro facts, lists, see turn off etc
import serverHttp1 as       sh1     # Servers for HTTP - User Support
import serverHttp2 as       sh2     # Servers for HTTP - Protein viewing
import specialFunction as   sf      # Classes and stuff for a very complex BP viewer
import manageSequences as   ms      # More stabler new ideas getting tried out and moved in
import taskingFunction as   tf      # Tasker for real timeish event processor calls. Has two versions both work
import toastMaker as        tm      # Notifications
import transFormations as   xf      # Sequence transFormations from mother natures ideas like DNA and RNA
import unlovedMenus as      um      # Pretty rarely used ond fashioned menus. A while interface is in here that works
import wayOffline as        wo      # Code not discarded but just studies, etc
import windowsX as          wx      # Windows Life ! X11 esp TK not MS Windoze ...

  
# When timestamp is easy stuff like human readable Feb23 bc-pierogi
def getHumanReadableTimestamp( aKind ):

    # When in human readables

    ans = ''                                                                            # Empty is rational, but not used much

    # A datetime object
    rNow = datetime.now()
 
    # Date and HHMMSS local time
    dt_1 = rNow.strftime( "%d-%m-%Y %H:%M:%S" )
    dt_2 = rNow.strftime( "%d-%m-%Y %H:%M:%f" )
    dt_3 = rNow.strftime( "%H:%M:%S %f" )
    dt_4 = rNow.strftime( "%H:%M:%S %f" ); dt_4 = dt_4[ 0: -3 ]
    dt_5 = rNow.strftime( "%H:%M:%S" )
    dt_6 = rNow.strftime( "%H:%M:%S" )
    dt_7 = rNow.strftime( "-%Y_%m_%d-%H%M%S" )
    dt_8 = rNow.strftime( "%Y_%m_%d-%H%M%S" )

    # Not usually a string
    dt_Z = rNow.strftime( "%Y%H%M%H%M%S" )

    # Different included fields is selectable
    if sb.isThisInHere( aKind, 'usual' ):
        ans = dt_1
        return ans

    if sb.isThisInHere( aKind, gi.kTIMESTAMPED ):
        ans = dt_7
        return ans

    if sb.isThisInHere( aKind, gi.kINTTS ):
        ans = int( dt_Z )
        return ans

    if sb.isThisInHere( aKind, gi.kUTIME ):        
        ans = dt_4    

    if sb.isThisInHere( aKind, gi.kFILESAVING ):
        ans = dt_1

    if sb.isThisInHere( aKind, gi.kTSHMS ):        
        ans = dt_5

    if sb.isThisInHere( aKind, gi.kHHMMSS ):        
        ans = dt_6    

    if sb.isThisInHere( aKind, gi.kNODASHTS ):        
        ans = dt_8    

    return ans


"""

Fun started here May 2022

"""