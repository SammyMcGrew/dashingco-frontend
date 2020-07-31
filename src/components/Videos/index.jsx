import React from 'react';
import ReactPlayer from 'react-player';
import './style.scss';



const ResponsivePlayer = ({ url, onProgress }) => {

    return (
        <div className='player-wrapper'>
            <ReactPlayer 
            className='react-player'
            url={url}
            width='50%'
            height='50%'
            controls={true}
            onProgress={onProgress}
            />
        </div>
      
    )

}


export default ResponsivePlayer;