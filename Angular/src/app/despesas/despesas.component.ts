import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-despesas',
  templateUrl: './despesas.component.html',
  styleUrls: ['./despesas.component.scss']
})
export class DespesasComponent implements OnInit {
  despesas:any;

  constructor(private apiService:ApiService ) { }
  ngOnInit() {
    this.apiService.getDespesas().subscribe((data)=>{
      console.log(data);
      this.despesas = data;
      console.log(this.despesas[0])
    });
  }
}
