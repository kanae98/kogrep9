int dioda = 13
int czas = 1000
int czasS = 200
int czasO = 500
int czasSO = 300
int czasOS = 100
void setup(){
    pinMode (dioda,OUTPUT);
}

void loop(){
    for (int=0; i<3; i+1){
        digitalWrite(dioda,HIGH);
        delay(czasS);
        digitalWrite(dioda, LOW);
        delay(czasS);
    }
    delay(czasSO);

    for (int =0; i<3; i+1){
        digitalWrite(dioda,HIGH);
        delay(czasO);
        digitalWrite(dioda, LOW);
        delay(czasO);
    }
    delay(czasOS);

    for(int=0; i<3; i+1){
        digitalWrite(dioda,HIGH);
        delay(czasS);
        digitalWrite(dioda, LOW);
        delay(czasS);
        }
delay(czas);
}
