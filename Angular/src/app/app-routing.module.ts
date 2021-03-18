import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PessoasComponent } from './pessoas/pessoas.component';
import { PessoasadicionarComponent } from './pessoasadicionar/pessoasadicionar.component';
import { PessoaseditarComponent } from './pessoaseditar/pessoaseditar.component';
import { ImovelComponent } from './imovel/imovel.component';
import { ImoveladicionarComponent } from './imoveladicionar/imoveladicionar.component';
import { ClientesComponent } from './clientes/clientes.component';
import { ClientesadicionarComponent } from './clientesadicionar/clientesadicionar.component';
import { DespesasComponent } from './despesas/despesas.component';
import { DespesasadicionarComponent } from './despesasadicionar/despesasadicionar.component';



const routes: Routes = [
  {path: 'pessoas', component: PessoasComponent},
  {path: 'pessoasadicionar', component: PessoasadicionarComponent},
  {path: 'pessoaseditar', component: PessoaseditarComponent},
  {path: 'imovel', component: ImovelComponent},
  {path: 'imoveladicionar', component: ImoveladicionarComponent },
  {path: 'clientes', component: ClientesComponent },
  {path: 'clientesadicionar', component: ClientesadicionarComponent },
  {path: 'despesas', component: DespesasComponent},
  {path: 'despesasadicionar', component: DespesasadicionarComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
