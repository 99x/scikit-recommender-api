import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'sc-output',
  templateUrl: './output.component.html',
  styleUrls: ['./output.component.scss']
})
export class OutputComponent implements OnInit {

  constructor() {
    // Do stuff
  }

  ngOnInit() {
    console.log('Output works fine!');
  }

}
