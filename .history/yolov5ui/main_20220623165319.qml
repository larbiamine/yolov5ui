import QtQuick 6.2
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15
import QtQuick.Dialogs
import Qt.labs.platform as PlatformControls
import QtMultimedia 


import QtQuick.Layouts

ApplicationWindow{
    id: window 
    x: 100
    y: 0
    width: 1000
    height: 800
    visible: true
    title: qsTr("Smart Parking")
    
    // SET FLAGS
    flags: Qt.WindowSystemMenuHint|  Qt.FramelessWindowHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint

    // SET MATERIAL STYLE
    Material.theme: Material.Dark
    Material.accent: Material.Teal

    MouseArea{
        id: mouseRegion
        anchors.fill: parent;
        property variant clickPos: "1,1"

        onPressed: {
            clickPos  = Qt.point(mouse.x,mouse.y)
        }

        onPositionChanged: {
            var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y)
            window.x += delta.x;
            window.y += delta.y;
        }
    }

    Button{
        id: minimizeButton
        flat : true
        width: 40
        text: qsTr("___")
        anchors.right: parent.right

        hoverEnabled: false
        onClicked:{
            window.showMinimized()
        }   
    }
    
    // CREATE TOP BAR
    Rectangle{
        id: topBar
        height: 40
        color: Material.color(Material.Teal)
        anchors{
            left: parent.left
            right: parent.right
            top: minimizeButton.bottom
            topMargin : 15
        }
       // radius: 10

        Text{
            text: qsTr("Smart Parking")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            color: "#ffffff"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 12
            font.bold: true
        }
    }
    Text{
        id: chooseType
        text: qsTr("Source")
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.topMargin: 20
        font.pointSize: 12
    }
    RowLayout  {
        id : chooseTypeRadio
        spacing: 0

        RadioButton {
            id: webcamradio
            text: qsTr("Camera")

        }

        RadioButton {
            id: imageradio
            checked: true
            text: qsTr("Image")
        }
        RadioButton {
            id: videoradio
            text: qsTr("Video")
        }

        RadioButton {
            id: directoryradio
            text: qsTr("Directory")
        }
        anchors.topMargin: 10 
        anchors.top: chooseType.bottom
        anchors.horizontalCenter: parent.horizontalCenter
    }
    Text{
        id: chooseModel
        text: qsTr("Modele")
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: chooseTypeRadio.bottom
        anchors.topMargin: 20
        font.pointSize: 12
    }
    RowLayout  {
        id : chooseModelRadio
        spacing: 0

        RadioButton {
            id: bdba
            text: qsTr("BDBA")
        }

        RadioButton {
            id: pklot
            checked: true
            text: qsTr("PKlot")
        }

        anchors.topMargin: 10 
        anchors.top: chooseModelType.bottom
        anchors.horizontalCenter: parent.horizontalCenter
    }


    // Source File
    MenuItem {
        
        id: source
        text: "Source: (Parcourir..)"
        onTriggered: {
            if(directoryradio.checked){
                
                sourceFolderDialog.open()
            }else{
                sourceFileDialog.open()
            }
        }
        width: 300
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: chooseTypeRadio.bottom
        anchors.topMargin: 25
        visible: !webcamradio.checked
    }



    FileDialog {
        id: sourceFileDialog
        title : "Open Source File"   

    }

    PlatformControls.FolderDialog {
        id: sourceFolderDialog
        title : "Open Source Folder"
        options : PlatformControls.FolderDialog.ShowDirsOnly
    }

    Text{
        //text: qsTr(sourceFileDialog.currentFile.toString().replace(/^(file:\/{3})/,"") + sourceFolderDialog.currentFolder.toString().replace(/^(file:\/{3})/,""))
        //acceptLabel
        function sourceText (){
            if(directoryradio.checked){
                return qsTr(sourceFolderDialog.currentFolder.toString().replace(/^(file:\/{3})/,""))
            }else{
                return qsTr(sourceFileDialog.currentFile.toString().replace(/^(file:\/{3})/,""))
            }
        } 
        text: sourceText()
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: source.bottom
        font.pointSize: 10
        visible: !webcamradio.checked
    }

    Text{
        id: resulttext
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter    
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: source.bottom
        font.pointSize: 10
        anchors.topMargin: 20       
        anchors.bottomMargin: 10    
    }

    // Video {
    //     id: video
    //     width : 640
    //     height : 360
    //     source: "a.mp4"

    //     anchors.top: detectButton.bottom
    //     anchors.topMargin: 10 
    //     anchors.horizontalCenter: parent.horizontalCenter
    //     MouseArea {
    //         anchors.fill: parent
    //         onClicked: {
    //             video.play()
    //         }
    //     }
    //     visible: true
    //     focus: true
    //     Keys.onSpacePressed: video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
    //     Keys.onLeftPressed: video.seek(video.position - 5000)
    //     Keys.onRightPressed: video.seek(video.position + 5000)
    // }

    Image{
        id: image
        anchors.top: exitButton.bottom
        anchors.topMargin: 10 
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.PreserveAspectFit
        width: 640; height: 360
        visible : false
    }


    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // BUTTON LOGIN
    Button{
        id: detectButton
        width: 300
        text: qsTr("Detection")
        anchors.top: resulttext.bottom
        anchors.topMargin: 10          
        anchors.horizontalCenter: parent.horizontalCenter
        background: Rectangle {
                radius: 5
                color: parent.down ? "#3C7C76" :
                        (parent.hovered ? Material.color(Material.LightBlue) : Material.color(Material.Teal))
        }    
        onClicked:{
            var type;
            var model;
            if(webcamradio.checked){
                type = "webcam"

                backend.runYolo(type,"")
            }
            if(imageradio.checked){
                type = "image"
                console.log("image")                
                backend.runYolo(type,sourceFileDialog.currentFile.toString().replace(/^(file:\/{3})/,""))
                
            }
            if(videoradio.checked){
                type = "video"
                console.log("video")
                backend.runYolo(type,sourceFileDialog.currentFile.toString().replace(/^(file:\/{3})/,""))
                //backend.playVideo("")
            }
            if(directoryradio.checked){
                type = "directory"
                console.log("directory")
                backend.runYolo(type,sourceFolderDialog.currentFolder.toString().replace(/^(file:\/{3})/,""))
            }
        } 
    }



    Button{
        id: exitButton
        flat : true
        width: 100
        text: qsTr("Exit")

        anchors.top: detectButton.bottom
        anchors.topMargin: 10          
        anchors.horizontalCenter: parent.horizontalCenter
        background: Rectangle {
            radius: 5
            color: parent.down ? "#7A1D00" : (parent.hovered ? "#FF825C" : "#FF5722" )
        }  
        onClicked:{
            backend.leave()
        } 
        
    }

    Connections {
        target: backend
        function onDetectionEnd(boolvalue, result, msg) {
            if(boolvalue){
                image.source = result
                image.visible = true
                console.log(result)
                resulttext.text = msg
                resulttext.color = "#007a6c"

            } else{
                resulttext.text = "Error "
                resulttext.color = "#D84315"
            }
        }    
    }
}