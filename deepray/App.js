import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import {StatusBar} from 'expo-status-bar'
import {StyleSheet, Text, View, TouchableOpacity, Alert, ImageBackground, Image, Button} from 'react-native'
import {Camera} from 'expo-camera'
let camera: Camera
const Stack = createNativeStackNavigator();

function HomeScreen({ navigation: { navigate } }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Please upload X-ray image </Text>
      <Button
        onPress={() =>
          navigate('Upload X-ray Photo')
        }
        title="Take a Photo"
      />
    </View>
  );
}

function GetDiagnosis({ navigation, route}) {

  const image_uri = route.params.photo
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      
      <Text 
      style={styles.titleText}
    >Hernia [83%]</Text>
      {image_uri && <Image source={{ uri: image_uri }} style={{ width: 250, height: 300 }} />}
      <Text style={styles.contentText}>A hernia is the abnormal exit of tissue or an organ, such as the bowel, through the wall of the cavity in which it normally resides. Various types of hernias can occur, most commonly involving the abdomen, and specifically the groin. Groin hernias are most commonly of the inguinal type but may also be femoral.</Text>
      
      
      <Button title="Go Back" onPress={() => navigation.goBack()} />
      <Button title="Home" onPress={() => navigation.navigate('Upload X-ray Photo')} />
     
    </View>
  );
}


function TakePhoto({ navigation: { navigate } }){
  
  const [startCamera, setStartCamera] = React.useState(false)
  const [previewVisible, setPreviewVisible] = React.useState(false)
  const [capturedImage, setCapturedImage] = React.useState(null)
  const [cameraType, setCameraType] = React.useState(Camera.Constants.Type.back)
  const [flashMode, setFlashMode] = React.useState('off')
  const __startCamera = async () => {
      const {status} = await Camera.requestPermissionsAsync()
      console.log(status)
      if (status === 'granted') {
        setStartCamera(true)

      } else {
        Alert.alert('Access denied')
      }
    }
  const __takePicture = async () => {
    const photo = await camera.takePictureAsync()
    console.log(photo)
    setPreviewVisible(true)
    //setStartCamera(false)
    setCapturedImage(photo)
  }
  const __savePhoto = () => {
    console.log('Clicked save photo',capturedImage)
    navigate('Diagnose',{photo:capturedImage.uri})
    Alert.alert('Disclaimer', 'This is an automated analysis. Before choosing any treatment, discuss these results with a trained medical professional.')
        
    // setStartCamera(false)
    }
  const __retakePicture = () => {
    setCapturedImage(null)
    setPreviewVisible(false)
    __startCamera()
  }
  const __handleFlashMode = () => {
    if (flashMode === 'on') {
      setFlashMode('off')
    } else if (flashMode === 'off') {
      setFlashMode('on')
    } else {
      setFlashMode('auto')
    }
  }
  const __switchCamera = () => {
    if (cameraType === 'back') {
      setCameraType('front')
    } else {
      setCameraType('back')
    }
  }
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  }
})
const CameraPreview = ({photo, retakePicture, savePhoto}) => {
  console.log('sdsfds', photo)
  
  return (
    <View
      style={{
        backgroundColor: 'transparent',
        flex: 1,
        width: '100%',
        height: '100%'
      }}
    >
      <ImageBackground
        source={{uri: photo && photo.uri}}
        style={{
          flex: 1
        }}
      >
        <View
          style={{
            flex: 1,
            flexDirection: 'column',
            padding: 15,
            justifyContent: 'flex-end'
          }}
        >
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'space-between'
            }}
          >
            <TouchableOpacity
              onPress={retakePicture}
              style={{
                width: 130,
                height: 40,

                alignItems: 'center',
                borderRadius: 4
              }}
            >
              <Text
                style={{
                  color: '#fff',
                  fontSize: 20
                }}
              >
                Re-take
              </Text>
            </TouchableOpacity>
            
              <Button
                style={{
                  width: 130,
                  height: 40,

                  alignItems: 'center',
                  borderRadius: 4
                }}
                onPress={__savePhoto}
                title="Get Diagnosis"
              />
          
          </View>
        </View>
      </ImageBackground>
    </View>
  )
}


  return (
    <View style={styles.container}>
      {startCamera ? (
        <View
          style={{
            flex: 1,
            width: '100%'
          }}
        >
          {previewVisible && capturedImage ? (
            <CameraPreview photo={capturedImage} savePhoto={__savePhoto} retakePicture={__retakePicture} />
          ) : (
            <Camera
              type={cameraType}
              flashMode={flashMode}
              style={{flex: 1}}
              ref={(r) => {
                camera = r
              }}
            >
              <View
                style={{
                  flex: 1,
                  width: '100%',
                  backgroundColor: 'transparent',
                  flexDirection: 'row'
                }}
              >
                <View
                  style={{
                    position: 'absolute',
                    left: '5%',
                    top: '10%',
                    flexDirection: 'column',
                    justifyContent: 'space-between'
                  }}
                >
                  <TouchableOpacity
                    onPress={__handleFlashMode}
                    style={{
                      backgroundColor: flashMode === 'off' ? '#000' : '#fff',
                      borderRadius: '50%',
                      height: 25,
                      width: 25
                    }}
                  >
                    <Text
                      style={{
                        fontSize: 20
                      }}
                    >
                      ⚡️
                    </Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    onPress={__switchCamera}
                    style={{
                      marginTop: 20,
                      borderRadius: '50%',
                      height: 25,
                      width: 25
                    }}
                  >
                    <Text
                      style={{
                        fontSize: 20
                      }}
                    >
                      {cameraType === 'front' ? '🤳' : '📷'}
                    </Text>
                  </TouchableOpacity>
                </View>
                <View
                  style={{
                    position: 'absolute',
                    bottom: 0,
                    flexDirection: 'row',
                    flex: 1,
                    width: '100%',
                    padding: 20,
                    justifyContent: 'space-between'
                  }}
                >
                  <View
                    style={{
                      alignSelf: 'center',
                      flex: 1,
                      alignItems: 'center'
                    }}
                  >
                    <TouchableOpacity
                      onPress={__takePicture}
                      style={{
                        width: 70,
                        height: 70,
                        bottom: 0,
                        borderRadius: 50,
                        backgroundColor: '#fff'
                      }}
                    />
                  </View>
                </View>
              </View>
            </Camera>
          )}
        </View>
      ) : (
        <View
          style={{
            flex: 1,
            backgroundColor: '#fff',
            justifyContent: 'center',
            alignItems: 'center'
          }}
        >
          <TouchableOpacity
            onPress={__startCamera}
            style={{
              width: 130,
              borderRadius: 4,
              backgroundColor: '#14274e',
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
              height: 40
            }}
          >
            <Text
              style={{
                color: '#fff',
                fontWeight: 'bold',
                textAlign: 'center'
              }}
            >
              Take picture
            </Text>
          </TouchableOpacity>
        </View>
      )}

      <StatusBar style="auto" />
    </View>
  )
}

const styles={
  titleText:{
    fontSize: 25,
    fontWeight: 'bold',
  },
  contentText:{
    margin:'5%'
  },
  
  }

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Upload X-ray Photo">
        <Stack.Screen name="Deep-ray" component={HomeScreen} />
        <Stack.Screen name="Upload X-ray Photo" component={TakePhoto} />
        <Stack.Screen name="Diagnose" component={GetDiagnosis} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
