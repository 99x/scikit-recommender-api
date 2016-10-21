import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'sc-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.scss']
})
export class InputComponent implements OnInit {

  constructor() {
    // Do stuff
  }

  ngOnInit() {
    console.log('Hello Input');
  }

}
