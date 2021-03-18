import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-clientesadicionar',
  templateUrl: './clientesadicionar.component.html',
  styleUrls: ['./clientesadicionar.component.scss']
})
export class ClientesadicionarComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }


  insereNovoCliente(id_pessoa:string, endereco:string, complemento:string, cep:string, cidade:string, estado:string, id_banco:string){
    this.apiService.postPessoas({ "id_pessoa":id_pessoa, "endereco":endereco, "complemento":complemento, "cep": cep, "cidade":cidade,"estado":estado, "id_banco":id_banco}).subscribe(data => {
      console.log(data)
      },
      error => {
      console.log("Error", error);
      });
    }
}
