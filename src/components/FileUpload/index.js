import React, { Component } from 'react';
import firebase from "firebase";
import FileUploader from "react-firebase-file-uploader";
import { imagePickerOptions, getFileLocalPath } from '../../Utils/index.js';
import './style.scss';



class VideoPage extends Component {
    state = {
      video: " ",
      title: " ",
      isUploading: false,
      progress: 0,
      videoURL: " ",
    };
   
    
    handleUploadVideo = event =>
      this.setState({ video: event.target.value });
    handleUploadStart = () => this.setState({ isUploading: true, progress: 0 });
    handleProgress = progress => this.setState({ progress });
    handleUploadError = error => {
      this.setState({ isUploading: false });
      console.error(error);
    };
    handleUploadSuccess = filename => {
      this.setState({ video: filename, progress: 100, isUploading: false });
      firebase
        .storage()
        .ref("videos")
        .child(filename)
        .getDownloadURL()
        .then(url => this.setState({ videoURL: url }));
    };
   
    render() {
      return (
        <div>
          
          <form class = "uploader">
          <label style={{backgroundColor: 'blue', color: 'white', padding: 10, borderRadius: 4, cursor: 'pointer'}}> 
          <FileUploader 
              
              accept="media/*"
              name="video"
              randomizeFilename
              storageRef={firebase.storage().ref("videos")}
              onUploadStart={this.handleUploadStart}
              onUploadError={this.handleUploadError}
              onUploadSuccess={this.handleUploadSuccess}
              onProgress={this.handleProgress}
                
            />
              </label>
            {/* <input
              type="text"
              value={this.state.video}
              name="video"
              onChange={this.handleUploadVideo}
            />  */}
            <button onClick = {this.handleUploadSuccess}>Upload</button>
            {this.state.isUploading && <p>Progress: {this.state.progress}</p>}
            {this.state.videoURL && <video src={this.state.videoURL}  height = "300" width="300"/>} 
            <br/>
       
          </form>
          {/* <div>
          {this.state.downloadURLs.map((downloadURL, i) => {
            return <video key={i} src={downloadURL} />;
          })}
        </div> */}
        
        </div>
      );
    }
  }
   
  export default VideoPage;


