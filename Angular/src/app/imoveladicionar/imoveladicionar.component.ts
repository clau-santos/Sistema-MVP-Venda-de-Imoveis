import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-imoveladicionar',
  templateUrl: './imoveladicionar.component.html',
  styleUrls: ['./imoveladicionar.component.scss']
})
export class ImoveladicionarComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoImovel(tipo_imovel:string, endereco:string, complemento:string, cep:string, cidade:string, estado:string, id_pessoa:string, adquirido_em:string){
      this.apiService.postImovel({ "tipo_imovel":tipo_imovel, "endereco":endereco, "complemento":complemento, "cep":cep,"cidade":cidade, "estado":estado, "id_pessoa":id_pessoa, "adquirido_em":adquirido_em}).subscribe(data => {
        console.log(data)
        },
        error => {
        console.log("Error", error);
        });
  }
}

