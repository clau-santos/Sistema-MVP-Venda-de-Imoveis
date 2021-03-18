import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DespesasadicionarComponent } from './despesasadicionar.component';

describe('DespesasadicionarComponent', () => {
  let component: DespesasadicionarComponent;
  let fixture: ComponentFixture<DespesasadicionarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DespesasadicionarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DespesasadicionarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
