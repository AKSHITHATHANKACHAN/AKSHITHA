import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShareService {
  readonly APIUrl = "http://127.0.0.1:8000/";

  constructor(private http:HttpClient) { }

  getType(){
    return this.http.get(this.APIUrl+'app/data/');
  }
  getTotal(val:any){
    return this.http.post(this.APIUrl+'app/total/',val);
  }
  getCart(){
    return this.http.get(this.APIUrl+'app/getcart/');
  }

  addcart(val:any){
    return this.http.post(this.APIUrl+"app/task/",val)
  }
  update(val:any){
    return this.http.post(this.APIUrl+"app/update/",val)
  }
  deleteTask(data:any){
    return this.http.delete(this.APIUrl+"app/task/"+data)
  }

  Remove(data:any){
    return this.http.post(this.APIUrl+"app/remove/",data)
  }

  getData(val:any){
    return this.http.post(this.APIUrl+"app/getData/",val)
  }
  updatefilter(val:any){
    return this.http.put(this.APIUrl+"app/filter/",val)
  }
}

