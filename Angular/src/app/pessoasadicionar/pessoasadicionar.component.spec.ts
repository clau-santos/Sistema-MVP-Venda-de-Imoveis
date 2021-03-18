import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PessoasadicionarComponent } from './pessoasadicionar.component';

describe('PessoasadicionarComponent', () => {
  let component: PessoasadicionarComponent;
  let fixture: ComponentFixture<PessoasadicionarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PessoasadicionarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PessoasadicionarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
