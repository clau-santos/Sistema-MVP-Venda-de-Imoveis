import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImoveladicionarComponent } from './imoveladicionar.component';

describe('ImoveladicionarComponent', () => {
  let component: ImoveladicionarComponent;
  let fixture: ComponentFixture<ImoveladicionarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImoveladicionarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImoveladicionarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
