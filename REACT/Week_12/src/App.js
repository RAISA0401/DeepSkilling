import React, { Component } from "react";
import GuestPage from "./GuestPage";
import UserPage from "./UserPage";
import LoginButton from "./LoginButton";
import LogoutButton from "./LogoutButton";

class App extends Component {
  constructor() {
    super();

    this.state = {
      isLoggedIn: false,
    };
  }

  login = () => {
    this.setState({ isLoggedIn: true });
  };

  logout = () => {
    this.setState({ isLoggedIn: false });
  };

  render() {
    return (
      <div style={{ padding: "20px" }}>
        {this.state.isLoggedIn ? <UserPage /> : <GuestPage />}

        <br />

        {this.state.isLoggedIn ? (
          <LogoutButton onClick={this.logout} />
        ) : (
          <LoginButton onClick={this.login} />
        )}
      </div>
    );
  }
}

export default App;