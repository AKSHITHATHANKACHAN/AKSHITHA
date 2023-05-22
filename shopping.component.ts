import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-shopping',
  templateUrl: './shopping.component.html',
  styleUrls: ['./shopping.component.css']
})
export class ShoppingComponent implements OnInit {

  constructor(
    public router: Router
  ) { }

  ngOnInit(): void {

  }

  click(){
    this.router.navigate(['shopping'])
  }

}
