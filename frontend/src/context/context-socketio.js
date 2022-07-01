import { createContext, useState, useEffect } from 'react'
import { Manager } from "socket.io-client"

const Context = createContext({})

// export function ContextSocketProvider({children}) {
//     const [Socket, setSocket] = useState(null)
//     useEffect(() => {
//         const SOCKET_URL = "ws://localhost:5001"
//         const manager = new Manager(SOCKET_URL)
//         const socket = manager.socket('/')
//         setSocket(socket)
//         Socket.on("connect", () => {
//             console.log('socket.connectを出力')
//         })
//     }, [])
//     return <Context.Provider value={{Socket}}>{children}</Context.Provider>
// }

export default Context