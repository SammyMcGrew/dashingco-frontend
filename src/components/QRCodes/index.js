// import React from 'react';
// import QRCode from './node_modules/qrcode.react';

// const QRCode = props => {
  
// return ( 
// constructor (props) {
//     super(props);
// this.download = this.download.bind(this);
// }
// componentDidMount(){
//  this.download()
// }
// render() {
// return (
//  <div style={{display: "none"}} className="HpQrcode"> // hidden div
//    <QRCode
//      value={this.state.values._id}
//      size={128}
//      level={'H'}
//    />
//  </div>
//   <a ref={(ref: any): any => this.downloadRef = ref}>
//     Download QR Code
//   </a>
// )};

// download() {
//     const canvas: any = document.querySelector('.HpQrcode > canvas');
//     this.downloadRef.href = canvas.toDataURL();
//     this.downloadRef.download = this.state.values.deviceId + "-QR.png";
// }
// }
// export default QRCode;

import React from 'react'
import QrCode from 'react.qrcode.generator'
 
const QRCode = props => {
  
    return (
    <div>
      <QrCode value='https://reactjs.org'/>
    </div>
    )
  }

export default QRCode;