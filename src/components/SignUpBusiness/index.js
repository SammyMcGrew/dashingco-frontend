import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { signUpUserBusiness } from './../../redux/User/user.actions';
import './style.scss';

import AuthWrapper from './../AuthWrapper';
import FormInput from './../Forms/FormInput';
import Button from './../Forms/Button';

const mapState = ({ user }) => ({
    currentUser: user.currentUser,
    userErr: user.userErr,
});

const SignupBusiness = props => {
    const { currentUser, userErr } = useSelector(mapState);
    const dispatch = useDispatch();
    const [displayName, setDisplayName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errors, setErrors] = useState('');

    useEffect(() => {
        if (currentUser) {
            reset();
            props.history.push('/');
        }
    }, [currentUser]);

    useEffect(() => {
        if (Array.isArray(userErr) && userErr.length > 0 ) {
         setErrors(userErr);
        }
         
     }, [userErr]);
 
     const reset = () => {
         setDisplayName('');
         setEmail('');
         setPassword('');
         setConfirmPassword('');
         setErrors([]);
     };

    const handleFormSubmit = event => {
        event.preventDefault();
        dispatch(signUpUserBusiness({
            displayName,
            email,
            password,
            confirmPassword
        }))

}
    const configAuthWrapper = {
    headline: 'businessRegistration'
};

return (
    <AuthWrapper {...configAuthWrapper}>
        <div className='formWrap'>

            {errors.length > 0 && (
                <ul>
                    {errors.map((err, index) => {
                        return (
                            <li key={index}>
                                {err}
                            </li>
                        );
                    })}
                </ul>
            )}

            <form onSubmit={handleFormSubmit}>

                <FormInput
                    type='text'
                    name='displayName'
                    value={displayName}
                    placeholder='Business Name'
                    handleChange={e => setDisplayName(e.target.value)}
                />

                <FormInput
                    type='email'
                    name='email'
                    value={email}
                    placeholder='Email'
                    handleChange={e => setEmail(e.target.value)}

                />

                <FormInput
                    type='password'
                    name='password'
                    value={password}
                    placeholder='Password'
                    handleChange={e => setPassword(e.target.value)}
                />

                <FormInput
                    type='password'
                    name='confirmPassword'
                    value={confirmPassword}
                    placeholder='Confirm Password'
                    handleChange={e => setConfirmPassword(e.target.value)}

                />

                <Button type='submit'>
                    Register Business
                </Button>
                
            </form>
        </div>
    </AuthWrapper>
);
}

export default withRouter(SignupBusiness);