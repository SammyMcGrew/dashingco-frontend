import React from 'react';
import ToggleButton from '../../components/SideDrawer/ToggleButton';
// import Drawer from '../../components/SideDrawer/Drawer';
import { Link } from 'react-router-dom';
//import { SocialMediaIconsReact } from 'social-media-icons-react';
import SideDrawer from '../../components/SideDrawer/index';
import './style.scss';

// import Logo from './../../assets/logo.png';

const Contact = props => {
    return (

<header className="toolbar">
    <nav className="toolbar_navigation">
        <div style={{height: '100%'}}>
            <ToggleButton />
            <SideDrawer />
        </div>

        <div className='toolbar_logo'><a href="/"> HOME </a></div>
        <div className='spacer' />
        <div className='toolbar_navigation_items'>
            <br />
            <br />
            <br />
            <ul>
                <li>
                    {/* <SocialMediaIconsReact icon="twitter" url */}
                    <a href="https://twitter.com/your-twitter-handle"> Twitter</a> 
                </li>
                <li>
                    {/* <SocialMediaIconsReact icon="facebook" url */}
                    <a href="https://facebook.com/Dashingco">Facebook</a>
                </li>
                <li>
                    {/* <SocialMediaIconsReact icon="instagram" url */}
                    <a href="https://instagram.com/Dashingco">Instagram</a>
                </li>
            </ul>

            <main style={{ marginTop: '20px' }}> 
                <p> Contact Us  </p>
                
            </main>
            
        </div>
    </nav>
</header>
);
}

export default Contact;

// import React from "react";
// import { useForm } from "react-hook-form";

// export default function App() {
//   const { register, handleSubmit } = useForm();
//   const onSubmit = data => console.log(data);
   
//   return (
//       <main>
//     <div className='formWrap'>
//      <form onSubmit={handleSubmit(onSubmit)}>
//       <input name="firstName" ref={register} />
//       <br/>
//       <input name="lastName" ref={register} />
//       <br/>
//       <select name="user" ref={register}>
//         <option value="business">Business</option>
//         <option value="jobSeeker">Job Seeker</option>
//       </select>
//       <br/>
//       <input type="submit" />
//     </form>
//     </div>
//     </main>
//   );
// }