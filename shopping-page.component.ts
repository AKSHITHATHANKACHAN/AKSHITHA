
import { Component, OnInit } from '@angular/core';
// import Swal from 'sweetalert2';
// import * as moment from 'moment';
import { ShareService } from 'src/app/share.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-shopping-page',
  templateUrl: './shopping-page.component.html',
  styleUrls: ['./shopping-page.component.css']
})
export class ShoppingPageComponent implements OnInit {
  data:any=[]
productA: any;
rateA: any;
  constructor(
    private service: ShareService,
    public router: Router


  ) { }

  ngOnInit(): void {

    this.service.getType().subscribe((res)=>{

      this.data = res
      console.log(this.data[0]['rate'],'hii')

  })
  }
  addClick(){
console.log('hii');
this.router.navigate(['cart'])
  }

  addCart(id: any){
    this.service.addcart(id).subscribe((data)=>{

        alert('Item is aaded in your Cart')
    })
  }
}
