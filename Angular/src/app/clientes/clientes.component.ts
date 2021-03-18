import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';


@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.scss']
})
export class ClientesComponent implements OnInit {
  clientes:any;
  pessoas:any;

  constructor(private apiService:ApiService ) { }
  ngOnInit() {
    this.apiService.getClientes().subscribe((data)=>{
      console.log(data);
      this.clientes = data;
      console.log(this.clientes[0])
    });
  }

}
