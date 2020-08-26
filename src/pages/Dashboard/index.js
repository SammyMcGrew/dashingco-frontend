import React from 'react';
import { Link } from 'react-router-dom';
import './style.scss';
import FileUploader from "react-firebase-file-uploader";
import {Table, Container, Grid, Row, Col, Image, Button} from 'react-bootstrap';
// import Button from './../../../../


// import QRcodes from '../../components/QRCodes';
import Lesson from '../../components/lesson';
import Videos from '../../components/Videos';
import Upload from '../../components/FileUpload';

const Dashboard = props => {
    return (

        <div className='dash'>
            <h1 >
                Welcome to your dashboard!
            </h1>
            
            <Container >
                <Row>
                    <Col className='resumelink'>
                        <Link to='/videogrid'>
                            Applicants Video Resumes
                        </Link>
                    </Col>
                </Row>
            </Container>
            <Container>
                <Row >
                    <Col lg = {true}>
                        <Lesson />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Videos />
                    </Col>
                </Row>
            </Container>
              
            
            
               
                
                
                {/* <QRcodes /> */}
                
                
        </div>
                
       
    );
    
};

export default Dashboard;