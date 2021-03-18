import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PessoasComponent } from './pessoas/pessoas.component';
import { PessoasadicionarComponent } from './pessoasadicionar/pessoasadicionar.component';
import { PessoaseditarComponent } from './pessoaseditar/pessoaseditar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ImovelComponent } from './imovel/imovel.component';
import { ImoveladicionarComponent } from './imoveladicionar/imoveladicionar.component';
import { ClientesComponent } from './clientes/clientes.component';
import { ClientesadicionarComponent } from './clientesadicionar/clientesadicionar.component';
import { MenuComponent } from './menu/menu.component';
import { DespesasComponent } from './despesas/despesas.component';
import { DespesasadicionarComponent } from './despesasadicionar/despesasadicionar.component';



@NgModule({
  declarations: [
    AppComponent,
    PessoasComponent,
    PessoasadicionarComponent,
    PessoaseditarComponent,
    ImovelComponent,
    ImoveladicionarComponent,
    ClientesComponent,
    ClientesadicionarComponent,
    MenuComponent,
    DespesasComponent,
    DespesasadicionarComponent,

  ],

  imports: [

    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }

