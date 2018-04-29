import React, { Component } from 'react';
import './App.css';
import Switch from './Switch.js'


class App extends Component {
  constructor(props) {
    super(props);

    // this.state contains all the state of the app. Redux could be
    // used if this grows.
    this.state = {
      lightOn: true,
    }
  }

  componentDidMount() {
    // Get the current state of the light from the server.
    this.getLightOn();
  }

  render() {
    const { lightOn } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to Light Controller</h1>
        </header>
        <p className="App-intro">
          A way to control your light from anywhere!
        </p>
        <Switch
          switchOn={lightOn}
          handleClick={(on) => this.setLightOn(on)}
        />
      </div>
    );
  }

  // setLightOn makes an API call to set the actual state of the light.
  setLightOn(on) {
    this.setState({ lightOn: on });
    fetch(
      `/api/setlight/${on}`, { method: 'POST' }
    ).then(
      (response) => {
        return response.json();
      }
    ).then(
      (response) => {
        if (response.status !== on) {
          this.setState({ lightOn: response.status });
        }
      }
    );
  }

  // getLightOn makes an API call to get the actual state of the light.
  getLightOn() {
    fetch(
      '/api/getlight', { method: 'GET' }
    ).then(
      (response) => {
        return response.json();
      }
    ).then(
      (response) => {
        this.setState({ lightOn: response.status });
      }
    );
  }
}

export default App;
