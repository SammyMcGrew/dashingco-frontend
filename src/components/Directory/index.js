import React from 'react';
import { Link } from 'react-router-dom';
import './style.scss';
//import Carousel from '../Carousel';

// import JobSeekers from './../../assets/jobSeekers.png';
// import Employers from './../../assets/employers.png';
// import Background from './../../assets/redBackground.png';

// import QRCode from '../QRCodes';

const Directory = props => {
    return (
        <div className='directory'>

            <div className='wrap'>
                <div className='item'
                // style={{
                //     backgroundImage: `url(${Background})`
                // }}              
                > 
                {/* <Carousel /> */}
                    <div className='jobSearch'>
                        <Link to='/about'>
                            Why Go Dashing?
                        </Link>
                        {/* <a>
                    © Dashing 2020
           </a> */}
                        {/* <QRCode /> */}
                    </div>
                   
                    </div>
              
                {/* <div className='item'
                    style={{
                        backgroundImage: `url(${Employers})`
                    }}
                >
                    <a>
                        Employers
              </a>
                </div> */}
            </div>
        </div>
    );
};

export default Directory;