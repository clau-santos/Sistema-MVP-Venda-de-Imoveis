import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-pessoasadicionar',
  templateUrl: './pessoasadicionar.component.html',
  styleUrls: ['./pessoasadicionar.component.scss']
})
export class PessoasadicionarComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovaPessoa(nome:string, datanascimento:string, cpf:string, rg:string, telefone:string, estado_civil:string, profissao:string){
      this.apiService.postPessoas({ "nome":nome, "data_nascimento":datanascimento, "cpf":cpf, "rg":rg,"telefone":telefone, "estado_civil":estado_civil, "profissao":profissao}).subscribe(data => {
        console.log(data)
      },
      error => {
      console.log("Error", error);
      });
  }
}
