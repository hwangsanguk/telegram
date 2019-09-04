/*
axios를 활용하여 
https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874
요청을 보내,
1등 번호 6개가 담긴 winner배열을 만들어 출력하세요.

*/

const axios = require('axios')


// const winner = [];


//   axios.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874')
//   .then( response => { 
//             for(let i=1; i<7; i++) {
//                 let name = 'drwtNo'+i;
//                 winner.push(response.data[name])
//             }
//             console.log(winner)
//             console.log(response.data); } ) 
//   .catch( err => { console.log(err); } );


  //강사님
  url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'
  axios.get(url)
  .then((res)=>{
      let winner =[];
      for(let i =0 ; i<6 ; i ++){
        winner.push(res.data[`drwtNo${i+1}`])

      }
      


      console.log(winner);
      
  })