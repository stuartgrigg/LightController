import React, { Component } from 'react';
import PropTypes from 'prop-types';
import switchOnImg from './switch--on.png';
import switchOffImg from './switch--off.png';
import './Switch.css'

// Switch is a component that renders a button with a picture
// of an on/off switch. The component is not stateful, with the
// state of the switch and the action to be performed when it is
// pressed controlled by its props.
class Switch extends Component {
  render() {
    const { switchOn, handleClick } = this.props;
    return (
      <img 
        src={this.getImageSrc()}
        className="Switch-logo"
        onClick={()=>handleClick(!switchOn)}
        alt=""
      />
    );
  }

  getImageSrc(){
    return this.props.switchOn ? switchOnImg : switchOffImg;
  }
}

Switch.propTypes = {
  // switchOn represents whether the switch should be rendered as on.
  switchOn: PropTypes.bool.isRequired,

  // handleClick is a callback to handle the switch being clicked. It
  // takes the inverse of switchOn at the time of clicking.
  handleClick: PropTypes.func.isRequired
}

export default Switch;