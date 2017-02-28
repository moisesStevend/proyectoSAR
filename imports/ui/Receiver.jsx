import React,{Component} from 'react'
import mqtt from 'wt-mqtt'

export default class Receiver extends Component{
  constructor(props){
    super(props);
    this.state={
      data: [],
    }
  }
  componentWillMount() {
    this.client=mqtt.connect('ws://10.10.40.185:9001')
    this.client.subscribe('sar')

    this.client.on('connect',()=>{
      console.log("mqtt conectado")
    })

    this.client.on('message',(topic,payload)=>{
      let json_payload=JSON.parse(payload)

      console.log(json_payload)

      let json_data=JSON.parse(json_payload.data)
      console.log(json_data)
      console.log(json_data[0])
      console.log(typeof(json_data))

      this.setState({
        data: json_data
      })
    })
  }//fin del componentWillMount
  render(){
    return(
      <div>
        {this.state.data}
      </div>
    );
  }
}

/*
import { Meteor } from 'meteor/meteor';

var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://10.10.40.185')

client.on('connect', function () {
  client.subscribe('presence')
})

client.on('message', function (topic, payload) {
  let json_payload=JSON.parse(payload)

  console.log(json_payload)

  let json_data=JSON.parse(json_payload.data)
  console.log(json_data)
  console.log(json_data[0])
  console.log(typeof(json_data))
  //client.end()
})


*/
