import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ShareService } from './share.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { SelectDropDownModule } from 'ngx-select-dropdown';
import { ShoppingComponent } from './shopping/shopping.component';
import { RouterModule } from '@angular/router';
import { ShoppingPageComponent } from './shopping-page/shopping-page.component';
import { CartpageComponent } from './cartpage/cartpage.component';


@NgModule({
  declarations: [
    ShoppingComponent,
    AppComponent,
    ShoppingPageComponent,
    CartpageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    SelectDropDownModule,
    RouterModule,



  ],
  providers: [ShareService],
  bootstrap: [AppComponent]
})
export class AppModule { }
