import { Component, OnInit } from '@angular/core';
import { ShareService } from 'src/app/share.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cartpage',
  templateUrl: './cartpage.component.html',
  styleUrls: ['./cartpage.component.css']
})
export class CartpageComponent implements OnInit {
  datacart: any =[]
  total: any=[]
  bln_gift =false
  constructor(
    private service: ShareService,
    public router: Router
  ) { }

  ngOnInit(): void {
    this.getData()
    this.getTotal()

  }
  getData(){
    this.service.getCart().subscribe((datas)=>{

      this.datacart =datas
    })
  }
  getTotal(){
    if(confirm("Do yo want Gift Warp")){
      let gift =1
    this.service.getTotal(gift).subscribe((total)=>{
      this.total=total
      if (this.total[0]['gift']){
        this.bln_gift =true
      }
    })
  }
  else{
    let gift =0
    this.service.getTotal(gift).subscribe((total)=>{
      this.total=total
    })
  }
}
added(item:any){
  this.service.update(item).subscribe((data)=>{
    this.getData()
    this.getTotal()
  })
}
remove(id:any){
  this.service.Remove(id).subscribe((status)=>{
    alert("Item is removed from your cart")
    this.getData()
    this.getTotal()
  })
}
Back(){
  this.router.navigate(['shop/shopping'])
}

}
