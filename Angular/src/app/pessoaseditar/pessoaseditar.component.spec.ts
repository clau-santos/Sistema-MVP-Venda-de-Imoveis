import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PessoaseditarComponent } from './pessoaseditar.component';

describe('PessoaseditarComponent', () => {
  let component: PessoaseditarComponent;
  let fixture: ComponentFixture<PessoaseditarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PessoaseditarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PessoaseditarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
