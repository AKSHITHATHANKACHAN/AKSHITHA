import { CartpageComponent } from './cartpage/cartpage.component';
import { ShoppingPageComponent } from './shopping-page/shopping-page.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ShoppingComponent } from './shopping/shopping.component';

const routes: Routes = [
  {path:'shop',
  component:ShoppingComponent},

  {path:'shop/shopping',
component:ShoppingPageComponent},
{path:'shop/shopping/cart',
component:CartpageComponent}
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
