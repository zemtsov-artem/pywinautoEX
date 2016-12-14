import time
import pywinauto
#Aliases
MainBundle = "TheWiresharkNetworkAnalyzer"
WireSharkDir = r"F:\Program Files (x86)\Wireshark\Wireshark.exe"
InterfaceName="Ethenet"
timeInterval = 1
#App open
app=pywinauto.Application(backend='uia')
app.start(WireSharkDir)
# wait till the window is really open
app[MainBundle].wait('visible')

menuBar=app[MainBundle].child_window(contol_type="MenuBar")

CaptureButton=menuBar.child_window(title="Capture")
app[MainBundle].child_window(title="Ethernet", control_type="TreeItem").wrapper_object().double_click_input()



time.sleep(timeInterval)
app["CapturingfromEthernet"].child_window(title="Stop", control_type="Button").wrapper_object().click_input()
app["*Ethenet"].child_window(title="1", control_type="TreeItem").wrapper_object().click_input()
#bad method - item_count()
app["*Ethenet"].child_window(title="1", control_type="TreeItem").parent().item_count()
#tree = app["*Ethenet"].ItemsView.wrapper_object()


print(app["*Ethenet"].child_window(title="Packet list Packet list", control_type="Tree"))
#print(app["*Ethenet"].child_window(title="Packet list Packet list", control_type="Tree").wrapper_object().get_item())

#it is a way to create array
print(app["*Ethenet"].child_window(title="Packet list Packet list", control_type="Tree").wrapper_object().children_texts())
#app.dialogs.print_control_identifiers()





#App close
#app.kill()
