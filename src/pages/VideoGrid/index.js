import firebase from "firebase";
import React, { Component } from 'react';
import ReactPlayer from 'react-player';
import ResponsivePlayer from '../../components/Videos';
import {Table, Container, Grid, Row, Col, Image, Button} from 'react-bootstrap';
import VideoPage from '../../components/FileUpload';

import './style.scss';


class VideoGrid extends Component {

    constructor (props) {
        super (props);
        this.state = {vids:[]}
    }

    render() {
        return (
            <div> 
                <Col>
                    <Row>
                       
                    </Row>
                </Col>
            <Container className = 'gridTest'>
                    
                    <Col>
                        <Row>
                            Video goes here.
                        </Row>
                    </Col>
                    <Col>
                        <Row>
                            Video goes here.
                        </Row>
                    </Col>
                     <Col>
                        <Row>
                            Video goes here.
                        </Row>
                       
                    </Col>
                    <Col>
                        <Row>
                            Video goes here.
                        </Row>
                    </Col>

            </Container>
            <Container className= 'gridTest'>
                <Col>
                    <Row>
                        Video goes here.
                    </Row>
                </Col>
                <Col>
                    <Row>
                        Video goes here.
                    </Row>
                </Col>
                <Col>
                    <Row>
                        Video goes here.
                    </Row>
                </Col>
                <Col>
                    <Row>
                        Video goes here.
                    </Row>
                </Col>

            </Container>
            </div>
            
                
            
                  

            
           
                   
            
        )
        
    }

        
}

export default VideoGrid;

