import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-pessoas',
  templateUrl: './pessoas.component.html',
  styleUrls: ['./pessoas.component.scss']
})

export class PessoasComponent implements OnInit {
  pessoas:any;

  constructor(private apiService: ApiService) { }

  getPeople(){
    this.apiService.getPessoas().subscribe((data)=>{
      console.log(data);
      this.pessoas = data; //TODO: Verificar
      console.log(this.pessoas[0])
    });
  }

  ngOnInit() {
    this.getPeople();

  }

  deletePeople(id_pessoa:any){
    this.apiService.deletePessoa(id_pessoa).subscribe(()=>{
      this.ngOnInit()
    }
    )
  }

}
