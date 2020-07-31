import React, { useState, useRef, useEffect } from 'react';
import learnESL from './../.././Assets/learnESL.jpg';

function Paypal() {
    const [paidFor, setPaidFor] = useState(false);
    const [loaded, setLoaded] = useState(false);
  
    let paypalRef = useRef();
  
    const product = {
      price: 500.99,
      description: 'ESL classes',
      img: { learnESL }
    };
  
    useEffect(() => {
      const script = document.createElement('script');
      script.src =
        'https://www.paypal.com/sdk/js?client-id=AXE_rYiWEu8u7OABudPbwnqVvF_n79pnn1L6C8d9rGLUsNc7Cfo9NL7TnUZlyz2hh__zxK133NTAWmDn'
      script.addEventListener('load', () => setLoaded(true));
      document.body.appendChild(script);
  
      if (loaded) {
        setTimeout(() => {
          window.paypal
            .Buttons({
              createOrder: (data, actions) => {
                return actions.order.create({
                  purchase_units: [
                    {
                      description: product.description,
                      amount: {
                        currency_code: 'USD',
                        value: product.price
                      }
                    }
                  ]
                });
              },
              onApprove: async (data, actions) => {
                const order = await actions.order.capture();
  
                setPaidFor(true);
  
                console.log(order);
              },
            })
            .render(paypalRef);
        });
      }
  
    });
  
    return (
      <div className="App">
  
        {paidFor ? (
          <div>
            <h1>Congratulations! You bought a key to your success in learning!</h1>
            <img src={learnESL} />
          </div>
        ) : (
            <div>
              <h1>
                {product.description} starting at ${product.price}
              </h1>
              <img src={learnESL} width='200' />
              <div ref={v => (paypalRef = v)} />
            </div>
  
          )}
  
      </div>
  
    );
  
  }

  export default Paypal;