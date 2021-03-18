import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientesadicionarComponent } from './clientesadicionar.component';

describe('ClientesadicionarComponent', () => {
  let component: ClientesadicionarComponent;
  let fixture: ComponentFixture<ClientesadicionarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientesadicionarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientesadicionarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
