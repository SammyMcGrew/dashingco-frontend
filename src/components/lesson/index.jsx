import React, { useState } from 'react';
import './style.scss';
import ResponsivePlayer from '../Videos';

const Lesson = () => {

    const [watchComplete, setWatchComplete] = useState(false)
    
    const handleWatchComplete = ({ played }) => {
        if (played >= 0.8 && !watchComplete) {
            setWatchComplete(true)
        };
    }

    return (
    <div>
        <ResponsivePlayer 
        id = 'lesson'
        url='https://www.youtube.com/watch?v=C9OPFh4LHHw'
        onProgress={handleWatchComplete}
        />
        <div className={watchComplete ? 'marker marker--is-complete' 
        : 'marker marker--not-complete'}
        >
            Completed
        </div>
    </div>
    )
}

export default Lesson;