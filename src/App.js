import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Switch, Route } from 'react-router-dom';
import { checkUserSession } from './redux/User/user.actions';
import 'bootstrap/dist/css/bootstrap.css';

// components 
import AdminToolbar from './components/AdminToolbar';

// import Navbar from './components/Navbar';
//hoc
import WithAuth from './hoc/withAuth';
import WithAdminAuth from './hoc/withAdminAuth';
//layout
import MainLayout from './layouts/MainLayout';
import HomePageLayout from './layouts/HomepageLayout';
//pages
import Homepage from './pages/Homepage';
import Contact from './pages/Contact';
import About from './pages/About';
import Registration from './pages/Registration';
import BusinessRegistration from './pages/BusinessRegistration';
import Login from './pages/Login';
import Recovery from './pages/Recovery';
import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';
import VideoGrid from './pages/VideoGrid';
import './default.scss';

const App = props => {
  const dispatch = useDispatch();


  useEffect(() => {
    dispatch(checkUserSession());


  }, []);
return (
  <div className="App">
    <AdminToolbar />
    <Switch>
      < Route exact path='/' render={() => (
        <HomePageLayout>
          <Homepage />
        </HomePageLayout>
      )}
      />
      < Route path='/registration' render={() => (
        <MainLayout>
          <Registration />
        </MainLayout>
      )} />
    

      < Route path='/businessregistration' render={() => (
        <MainLayout>
          <BusinessRegistration />
        </MainLayout>
      )} />

      < Route path='/login'
        render={() => (
          <MainLayout>
            <Login />
          </MainLayout>
        )} />
          < Route path='/about'
        render={() => (
          <MainLayout>
            <About />
          </MainLayout>
        )} />
       < Route path='/contact'
        render={() => (
          <MainLayout>
            <Contact />
          </MainLayout>
        )} />
      <Route path='/recovery' render={() => (
        <MainLayout>
          <Recovery />
        </MainLayout>
      )} />
       {/* <Route path='/paypal' render={() => (
        <MainLayout>
          <Paypal />
        </MainLayout>
      )} /> */}
      <Route path='/dashboard' render={() => (
        <WithAuth>
          <MainLayout>
            <Dashboard />
          </MainLayout>
        </WithAuth>
      )} />
      <Route path='/admin' render={() => (
        <WithAdminAuth>
          <MainLayout>
            <Admin />
          </MainLayout>
        </WithAdminAuth>
      )} />
       <Route path='/videogrid' render={() => (
        /* <WithAdminAuth> */
          <MainLayout>
            <VideoGrid />
          </MainLayout>
        /* </WithAdminAuth> */
      )} />
    </Switch>
  </div>
  );
}

export default App;
