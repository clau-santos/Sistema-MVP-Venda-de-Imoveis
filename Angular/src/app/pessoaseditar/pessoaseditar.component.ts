import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-pessoaseditar',
  templateUrl: './pessoaseditar.component.html',
  styleUrls: ['./pessoaseditar.component.scss']
})
export class PessoaseditarComponent implements OnInit {
  pessoa:any
  constructor(private activatedRoute: ActivatedRoute, private apiService: ApiService) {
    this.activatedRoute.queryParams.subscribe(params => {
      this.carregaPessoa(Number(params['id_pessoa']))

  });

}

  ngOnInit(): void {
  }

  carregaPessoa(id_pessoa:number){
    console.log(id_pessoa);
    this.apiService.putPessoa(id_pessoa).subscribe(data => {
      console.log(data);
      this.pessoa = data;
      console.log(this.pessoa[0])
    },
    error => {
      console.log("Error", error)
    });
  }

  alteraPessoa(nome:string, datanascimento:string, cpf:string, rg:string, telefone:string, estado_civil:string, profissao:string){

  }
}
