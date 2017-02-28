import React,{Component} from 'react'
import mqtt from 'wt-mqtt'
import Receiver from './Receiver.jsx'

export default class App extends Component{
  render(){
    return(
      <div>
        <p>hello world!!</p>
        <Receiver/>
      </div>
    );
  }
}
