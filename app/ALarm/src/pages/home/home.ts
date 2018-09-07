import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  events:any;

  constructor(public navCtrl: NavController) {
    this.events = [
        {
            "event": "metal_alarm",
            "id": "de305d54-75b4-431b-adb2-eb6b9e546014",
            "time": "2018-09-07T14:43:57.351Z",
            "group": "A",
            "units": [1],
            "image": "https://picsum.photos/200?random"
        },
        {
            "event": "metal_alarm",
            "id": "2de5ff5a-29fd-4e46-8ee1-ff2538be72f5",
            "time": "2018-09-07T15:43:57.351Z",
            "group": "A",
            "units": [1],
            "image": "https://picsum.photos/200?random"
        },
        {
            "event": "metal_alarm",
            "id": "267e30e6-5963-4fad-81c9-9f3b4462c21a",
            "time": "2018-09-07T15:53:57.351Z",
            "group": "A",
            "units": [1],
            "image": "https://picsum.photos/200?random"
        }
    ]
  }
}
