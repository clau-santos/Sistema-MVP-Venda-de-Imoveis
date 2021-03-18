import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-despesasadicionar',
  templateUrl: './despesasadicionar.component.html',
  styleUrls: ['./despesasadicionar.component.scss']
})
export class DespesasadicionarComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }
  insereNovaDespesa(id_imovel:string, energia:string, agua:string, condominio:string, propaganda:string){
    this.apiService.postDespesa({ "id_imovel":id_imovel, "energia":energia, "agua":agua, "condominio": condominio, "propaganda":propaganda}).subscribe(data => {
      console.log(data)
      },
      error => {
      console.log("Error", error);
      });
    }
}
