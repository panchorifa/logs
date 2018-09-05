// import topResources from lib.processor
const topResources = require('../lib/processor')

const INPUT_1 = `
  [01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
  [01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
`

const INPUT_2 = `
  [01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
  [01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall2.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall3.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3631
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall6.gif HTTP/1.0" 200 3632
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall7.gif HTTP/1.0" 200 3633
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall8.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall34.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall35.gif HTTP/1.0" 200 3635
`

describe('log processor', () => {
  test('top resources with only a few logs', () => {
    const resources = topResources(INPUT_1)
    expect(resources.length).toEqual(2)
    expect(resources).toMatchSnapshot()
  })

  test('top resources with more than 10 logs', () => {
    const resources = topResources(INPUT_2)
    expect(resources.length).toEqual(10)
    expect(resources).toMatchSnapshot()
  })
})
