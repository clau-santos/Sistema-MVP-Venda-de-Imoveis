import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }

  public getPessoas(){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/pessoas`);
  }
  public postPessoas(pessoa:any){
    return this.httpClient.post(`http://127.0.0.1:5000/imobiliaria/pessoas`,pessoa );
  }
  public getPessoa(id_pessoa:any){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/pessoas/${id_pessoa}`);
  }

  public deletePessoa(id_pessoa:any){
    return this.httpClient.delete(`http://127.0.0.1:5000/imobiliaria/pessoa/${id_pessoa}`);
  }

  public putPessoa(id_pessoa:any){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/pessoas/${id_pessoa}`);
  }

  public getallImovel(){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/imovel`);
  }

  public postImovel(imovel:any){
    return this.httpClient.post(`http://127.0.0.1:5000/imobiliaria/imovel`,imovel);
  }

  public getClientes(){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/cliente`);
  }

  public postClientes(cliente:any){
    return this.httpClient.post(`http://127.0.0.1:5000/imobiliaria/cliente/adicionar`,cliente);
  }

  public getDespesas(){
    return this.httpClient.get(`http://127.0.0.1:5000/imobiliaria/despesas`);
}

public postDespesa(despesas:any){
  return this.httpClient.post(`http://127.0.0.1:5000/imobiliaria/despesas`,despesas);
}
}

