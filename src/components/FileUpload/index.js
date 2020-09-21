import React, { Component } from 'react';
import firebase from "firebase";
import './style.scss';
// import {ZiggeoPlayer} from 'react-ziggeo';


class VideoPage extends Component {
  state = {
   
  };
 
 // after react-ziggeo 3.3.0 version embedding argument also accessible
 playing = (embedding /* only starting from react-ziggeo 3.3.0 */) => {
  console.log('it\'s playing, your action here');
};

paused = (embedding /* only starting from react-ziggeo 3.3.0 */) => {
  console.log('it\'s paused, your action when pause');
};
 
  render() {
    return (
      <div>
      {/* <ZiggeoPlayer
      apiKey={'a293c346773385bae50fb960f2210d2d'}
      video={'Video Token'}
      theme={'modern'}
      themecolor={'red'}
      skipinitial={false}
      onPlaying={this.playing}
      onPaused={this.paused}
     
       /> */}
      </div>
    );
  }
}
 
export default VideoPage;